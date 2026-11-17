from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="0fb62a92-5423-5a34-b3cb-6635d7a39b58",
    key="BASE5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DarkKadabra.Name",
    display_name="Dark Kadabra",
    searchable_by=["Dark Kadabra", "Stage 1", "DarkKadabra"],
    subtypes=["Stage 1"],
    collector_number=39,
    set_code="BASE5",
    rarity=Rarities.Uncommon,
    hp=50,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Abra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Matter Exchange",
            game_text="Once during your turn (before your attack), you may discard a card from your hand in order to draw a card. This power can't be used if Dark Kadabra is Asleep, Confused, or Paralyzed.",
            effect=unimplemented,
        ),
        Attack(
            title="Mind Shock",
            game_text="Don't apply Weakness and Resistance for this attack. (Any other effects that would happen after applying Weakness and Resistance still happen.)",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=30,
            effect=unimplemented,
        ),
    ],
)