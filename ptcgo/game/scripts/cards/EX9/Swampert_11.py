from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.pokemon import is_water_energy
from ptcgo.game.card_effects.support_common import can_move_energy, move_energy_between
from ptcgo.game.content.definitions import Activations
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack, damage_all_opponents

water_cyclone = move_energy_between(
    is_water_energy, count=1, from_pool="active", to_pool="bench",
    prompt="Move a Water Energy to a Benched Pokémon",
)

card = PokemonCardDef(
    guid="3405b653-9144-512c-b91f-ab50220813cd",
    key="EX9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Swampert.Name",
    display_name="Swampert",
    searchable_by=["Swampert", "Stage 2", "Swampert"],
    subtypes=["Stage 2"],
    collector_number=11,
    set_code="EX9",
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marshtomp.Name",
    family_id=258,
    abilities=[
        Ability(
            title="Water Cyclone",
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy attached to 1 of your Active Pok\u00e9mon to 1 of your Benched Pok\u00e9mon. This power can't be used if Swampert is affected by a Special Condition.",
            effect=water_cyclone,
            activation=Activations.UNLIMITED,
            condition=can_move_energy(is_water_energy, from_pool="active", to_pool="bench"),
        ),
        Attack(
            title="Spinning Tail",
            game_text="Does 10 damage to each of your opponent's Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=damage_all_opponents(10),
        ),
        Attack(
            title="Aqua Sonic",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=ignore_modifier_attack(ignore_weakness=False),
        ),
    ],
)