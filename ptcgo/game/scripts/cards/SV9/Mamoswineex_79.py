from ptcgo.game.card_effects.trainers import is_pokemon_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="33368458-bd41-568f-99e0-d69101043df4",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mamoswineex.Name",
    display_name="Mamoswine ex",
    searchable_by=["Mamoswine ex", "Stage 2", "ex", "Mamoswineex"],
    subtypes=["Stage 2", "ex"],
    collector_number=79,
    set_code="SV9",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Piloswine.Name",
    family_id=220,
    abilities=[
        Ability(
            title="Mammoth Hauler",
            game_text="Once during your turn, you may search your deck for a Pok\u00e9mon, reveal it, and put it into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(predicate=is_pokemon_card, count=1, minimum=1),
        ),
        Attack(
            title="Rumbling March",
            game_text="This attack does 40 more damage for each Stage 2 Pok\u00e9mon on your Bench.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=180,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)