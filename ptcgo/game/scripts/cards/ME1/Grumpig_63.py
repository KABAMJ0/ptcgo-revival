from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import look_top_attach_energy
from ptcgo.game.card_effects.trainers import is_basic_energy_card

card = PokemonCardDef(
    guid="bcf0ce30-dde2-51c4-9ace-71aea1c89b9a",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Grumpig.Name",
    display_name="Grumpig",
    searchable_by=["Grumpig", "Stage 1", "Grumpig"],
    subtypes=["Stage 1"],
    collector_number=63,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Spoink.Name",
    family_id=325,
    abilities=[
        Ability(
            title="Energized Steps",
            game_text="Once during your turn, when you play this Pok\u00e9mon from your hand to evolve 1 of your Pok\u00e9mon, you may use this Ability. Look at the top 4 cards of your deck and attach any number of Basic Energy cards you find there to your Pok\u00e9mon in any way you like. Shuffle the other cards back into your deck.",
            trigger=Triggers.ON_EVOLVE,
            effect=look_top_attach_energy(4, predicate=is_basic_energy_card),
        ),
        Attack(
            title="Psychic Sphere",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)