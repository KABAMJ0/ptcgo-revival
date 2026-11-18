from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="29097bd7-5d59-5c9a-87a9-52b4614b677b",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Alakazam.Name",
    display_name="Alakazam",
    searchable_by=["Alakazam", "Stage 2", "Alakazam"],
    subtypes=["Stage 2"],
    collector_number=56,
    set_code="ME1",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Kadabra.Name",
    family_id=63,
    abilities=[
        Ability(
            title="Psychic Draw",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Draw 3 cards.",
            effect=unimplemented,
        ),
        Attack(
            title="Powerful Hand",
            game_text="Place 2 damage counters on your opponent's Active Pok\u00e9mon for each card in your hand.",
            cost={PokemonTypes.PSYCHIC: 1},
            effect=unimplemented,
        ),
    ],
)