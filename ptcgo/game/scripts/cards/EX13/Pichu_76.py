from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="856d2e66-75d3-5c72-8d09-3dd5d1fe9357",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pichu.Name",
    display_name="Pichu δ",
    searchable_by=["Pichu \u03b4", "Basic", "Pichu"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="EX13",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=172,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Pikachu from your hand onto Pichu (this counts as evolving Pichu) and remove all damage counters from Pichu.",
            effect=unimplemented,
        ),
        Attack(
            title="Paste",
            game_text="Search your discard pile for an Energy card and attach it to 1 of your Pok\u00e9mon that has \u03b4 on its card.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)