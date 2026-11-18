from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="35e9327a-fe1f-5907-b82c-2f8edf6b7578",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DelphoxBREAK.Name",
    display_name="Delphox BREAK",
    searchable_by=["Delphox BREAK", "BREAK", "DelphoxBREAK"],
    subtypes=["BREAK"],
    collector_number=14,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=180,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BREAK,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Delphox.Name",
    family_id=653,
    abilities=[
        Ability(
            title="Flare Witch",
            game_text="Once during your turn (before your attack), you may search your deck for a Fire Energy card and attach it to 1 of your Pok\u00e9mon. Shuffle your deck afterward.",
            effect=unimplemented,
        ),
    ],
)