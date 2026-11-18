from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import discard_then_draw
from ptcgo.game.card_effects.trainers import basic_energy_of

card = PokemonCardDef(
    guid="109809cb-899d-5bfc-ab45-1ccf0654717c",
    key="COL",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=17,
    set_code="COL",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Ability(
            title="Roast Reveal",
            game_text="Once during your turn (before your attack), you may discard a Fire Energy from your hand. If you do, draw 3 cards. This power can't be used if Ninetales is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            effect=discard_then_draw(1, 3, optional=True, predicate=basic_energy_of("fire")),
        ),
        Attack(
            title="Will-o'-the-wisp",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)