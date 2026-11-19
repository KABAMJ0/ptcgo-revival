from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import snipe_attack

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.attributes import AttrID

WATER = PokemonTypes.WATER.value


def _is_water_energy(card):
    return energy_provides_type(card, WATER)


def _wash_out_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    if board.active_pokemon(player_id) is None:
        return False
    bench = board.find_player_area(player_id, "bench")
    return any(_is_water_energy(energy)
               for p in (bench.children if bench else [])
               for energy in board.attached_energies(p))


card = PokemonCardDef(
    guid="df2c2524-c7c8-5335-a9fa-a922c596f5f0",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Blastoise.Name",
    display_name="Blastoise",
    searchable_by=["Blastoise", "Stage 2", "Blastoise"],
    subtypes=["Stage 2"],
    collector_number=13,
    set_code="HGSS2",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.LIGHTNING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Wartortle.Name",
    family_id=7,
    abilities=[
        Ability(
            title="Wash Out",
            game_text="As often as you like during your turn (before your attack), you may move a Water Energy attached to 1 of your Benched Pok\u00e9mon to your Active Pok\u00e9mon. This power can't be used if Blastoise is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_wash_out_available,
            effect=move_energy_between(predicate=_is_water_energy, count=1, from_pool="bench", to_pool="active"),
        ),
        Attack(
            title="Hydro Launcher",
            game_text="Return 2 Water Energy attached to Blastoise to your hand. Choose 1 of your opponent's Pok\u00e9mon. This attack does 100 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            effect=snipe_attack(100, pool="any", count=1, apply_modifiers=False),
        ),
    ],
)