from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import Passive, carrier_pokemon


class _FossilArmor(Passive):
    """Prevent attack damage of 60 or less done to Armaldo."""

    def prevents_damage(self, calc, carrier):
        if not (calc.is_attack and calc.is_opposing):
            return False
        if carrier_pokemon(carrier) is not calc.target:
            return False
        return 0 < calc.amount <= 60


async def _crush_claw(ctx):
    await ctx.deal_damage()
    defender = ctx.defender
    if defender is not None:
        ctx.add_damage_taken_modifier(40, defender, through="your_next_turn")


card = PokemonCardDef(
    guid="7550a1f7-0f5f-5fbc-8ad5-7184b47109c5",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armaldo.Name",
    display_name="Armaldo",
    searchable_by=["Armaldo", "Stage 2", "Armaldo"],
    subtypes=["Stage 2"],
    collector_number=18,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Anorith.Name",
    family_id=347,
    abilities=[
        Ability(
            title="Fossil Armor",
            game_text="If Armaldo would be damaged by an attack, prevent that attack's damage done to Armaldo if that damage is 60 or less.",
            passive=_FossilArmor(),
        ),
        Attack(
            title="Crush Claw",
            game_text="During your next turn, if an attack does damage to the Defending Pok\u00e9mon (after applying Weakness and Resistance), that attack does 40 more damage.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=_crush_claw,
        ),
    ],
)