from ptcgo.game.card_effects.attacks_common import self_energy_discard_attack
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.card_effects.trainers import basic_energy_of
from ptcgo.game.content.definitions import Activations
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


_DARKNESS_ENERGY = basic_energy_of("darkness")


card = PokemonCardDef(
    guid="20f4457b-d63c-59f4-987e-b9ce2946ae72",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name",
    display_name="Hydreigon",
    searchable_by=["Hydreigon", "Stage 2", "Hydreigon"],
    subtypes=["Stage 2"],
    collector_number=97,
    set_code="BW6",
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.DRAGON,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name",
    family_id=633,
    abilities=[
        Ability(
            title="Dark Trance",
            game_text="As often as you like during your turn (before your attack), you may move a Darkness Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon.",
            activation=Activations.UNLIMITED,
            condition=can_move_energy(_DARKNESS_ENERGY),
            effect=move_energy_between(_DARKNESS_ENERGY, count=1),
        ),
        Attack(
            title="Dragonblast",
            game_text="Discard 2 Darkness Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 2, PokemonTypes.COLORLESS: 1},
            damage=140,
            effect=self_energy_discard_attack(count=2, energy_type=PokemonTypes.DARKNESS),
        ),
    ],
)