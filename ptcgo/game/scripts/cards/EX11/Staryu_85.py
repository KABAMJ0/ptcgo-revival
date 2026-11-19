from ptcgo.game.card_effects.attacks_common import count_energy, flip_or_nothing
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities


async def _recover(ctx):
    staryu = ctx.attacker
    if staryu is None or count_energy("self", energy_type=PokemonTypes.WATER)(ctx) <= 0:
        return
    await ctx.discard_energy_from(staryu, 1, prompt="Discard a Water Energy")
    damaged = ctx.max_hp(staryu) - staryu.get_attribute(AttrID.HP, 0)
    if damaged > 0:
        await ctx.heal(min(40, damaged), staryu)

card = PokemonCardDef(
    guid="9319a64a-f193-537e-ba5a-879599ceb01c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staryu.Name",
    display_name="Staryu",
    searchable_by=["Staryu", "Basic", "Staryu"],
    subtypes=["Basic"],
    collector_number=85,
    set_code="EX11",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=120,
    abilities=[
        Attack(
            title="Surprise Attack",
            game_text="Flip a coin. If tails, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_or_nothing(),
        ),
        Attack(
            title="Recover",
            game_text="Discard a Water Energy card attached to Staryu and remove 4 damage counters from Staryu (all if there are less than 4).",
            cost={PokemonTypes.WATER: 1},
            effect=_recover,
        ),
    ],
)