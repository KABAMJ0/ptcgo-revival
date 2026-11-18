from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="43940e90-a227-5639-b5bb-cb6eefea54d9",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunala.Name",
    display_name="Lunala",
    searchable_by=["Lunala", "Stage 2", "Lunala"],
    subtypes=["Stage 2"],
    collector_number=102,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name",
    family_id=789,
    abilities=[
        Ability(
            title="Blessing of the Moone",
            game_text="Once during your turn (before your attack), if you have Solgaleo in play, you may search your deck for up to 2 Energy cards and attach them to your Solgaleo or Lunala in any way you like. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Lunar Blast",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=130,
        ),
    ],
)