from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import apply_own_next_turn_boost
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def _focus_energy(ctx):
    await ctx.deal_damage()
    await apply_own_next_turn_boost(ctx, 30, "Bite")

card = PokemonCardDef(
    guid="05fbb793-ba0c-5f56-a603-47c790ccbd05",
    key="HGSS4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Carvanha.Name",
    display_name="Carvanha",
    searchable_by=["Carvanha", "Basic", "Carvanha"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="HGSS4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=318,
    abilities=[
        Attack(
            title="Focus Energy",
            game_text="During your next turn, Carvanha's Bite attack's base damage is 40.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=_focus_energy,
        ),
        Attack(
            title="Bite",
            cost={PokemonTypes.DARKNESS: 1},
            damage=10,
        ),
    ],
)
