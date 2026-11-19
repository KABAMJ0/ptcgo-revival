from ptcgo.game.card_effects.trainers import is_basic_energy_card
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5eb538e9-6f74-5fae-bc56-ee138817a1bf",
    key="SM3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ribombee.Name",
    display_name="Ribombee",
    searchable_by=["Ribombee", "Stage 1", "Ribombee"],
    subtypes=["Stage 1"],
    collector_number=96,
    set_code="SM3",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    resistance_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cutiefly.Name",
    family_id=742,
    abilities=[
        Ability(
            title="Honey Gather",
            game_text="Once during your turn (before your attack), you may search your deck for up to 2 basic Energy cards, reveal them, and put them into your hand. Then, shuffle your deck.",
            activation=Activations.ONCE_PER_TURN,
            effect=search_to_hand(predicate=is_basic_energy_card, count=2, minimum=0),
        ),
        Attack(
            title="Pollen Shot",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)