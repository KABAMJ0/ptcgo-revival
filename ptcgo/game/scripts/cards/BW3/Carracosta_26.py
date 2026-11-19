from ptcgo.game.card_effects.passives_common import Passive
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.session.passives import carrier_pokemon


class _SolidRockPassive(Passive):
    """"If any damage is done to this Pokemon by attacks, flip a coin. If
    heads, reduce that damage by 50 (after Weakness and Resistance)."
    The library has flip-to-PREVENT only, so the flip-to-REDUCE interceptor is
    card-local here and filed for promotion."""

    def __init__(self, reduction=50, title="Solid Rock"):
        self.reduction = reduction
        self.title = title

    async def damage_interceptor(self, ctx, calc, target, carrier):
        if not (calc.is_attack and calc.is_opposing and calc.amount > 0):
            return None
        if carrier_pokemon(carrier) is not target:
            return None
        heads = await ctx.flip_coins(1, self.title,
                                     source=carrier_pokemon(carrier) or carrier)
        if heads and heads[0]:
            return max(0, calc.amount - self.reduction)
        return None


card = PokemonCardDef(
    guid="fdb22c97-f2ed-5b72-a3cf-b7e9ac53a2c3",
    key="BW3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name",
    display_name="Carracosta",
    searchable_by=["Carracosta", "Stage 1", "Carracosta"],
    subtypes=["Stage 1"],
    collector_number=26,
    set_code="BW3",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name",
    family_id=564,
    abilities=[
        Ability(
            title="Solid Rock",
            game_text="If any damage is done to this Pok\u00e9mon by attacks, flip a coin. If heads, reduce that damage by 50 (after applying Weakness and Resistance).",
            passive=_SolidRockPassive(),
        ),
        Attack(
            title="Crunch",
            game_text="Discard an Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
            effect=unimplemented,
        ),
    ],
)