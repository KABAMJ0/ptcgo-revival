from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

async def third_eye(ctx):
    """Discard an Energy from Dark Golduck to draw up to 3 cards."""
    gone = await ctx.discard_energy_from(ctx.attacker, 1,
                                         prompt="Discard an Energy from Dark Golduck")
    if not gone:
        return
    await ctx.draw_cards(3)

card = PokemonCardDef(
    guid="46764d09-7b8a-5d48-a920-17d2695fdb80",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkGolduck.Name",
    display_name="Dark Golduck",
    searchable_by=["Dark Golduck", "Stage 1", "DarkGolduck"],
    subtypes=["Stage 1"],
    collector_number=37,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Psyduck.Name",
    family_id=54,
    abilities=[
        Attack(
            title="Third Eye",
            game_text="Discard 1 Energy card attached to Dark Golduck in order to draw up to 3 cards.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=third_eye,
        ),
        Attack(
            title="Super Psy",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
        ),
    ],
)