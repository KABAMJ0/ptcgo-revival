from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e57a6a62-fa23-5ada-8d4f-3a6307635e05",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Wynaut.Name",
    display_name="Wynaut",
    searchable_by=["Wynaut", "Basic", "Wynaut"],
    subtypes=["Basic"],
    collector_number=42,
    set_code="DP1",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=360,
    abilities=[
        Ability(
            title="Baby Evolution",
            game_text="Once during your turn (before your attack), you may put Wobbuffet from your hand onto Wynaut (this counts as evolving Wynaut) and remove all damage counters from Wynaut.",
            effect=unimplemented,
        ),
        Attack(
            title="Astonish",
            game_text="Choose 1 card from your opponent's hand without looking. Look at the card you chose, then have your opponent shuffle that card into his or her deck.",
            cost={},
            effect=unimplemented,
        ),
    ],
)