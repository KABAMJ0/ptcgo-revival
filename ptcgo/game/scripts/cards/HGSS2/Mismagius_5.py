from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.attributes import AttrID

PSYCHIC = PokemonTypes.PSYCHIC.value


def _is_psychic_energy(card):
    return energy_provides_type(card, PSYCHIC)


def _move_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    holders = [p for p in board.pokemon_in_play(player_id)
               if any(_is_psychic_energy(e) for e in board.attached_energies(p))]
    return bool(holders) and len(board.pokemon_in_play(player_id)) >= 2


card = PokemonCardDef(
    guid="b26b49be-66ee-585b-8715-df84978a3704",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mismagius.Name",
    display_name="Mismagius",
    searchable_by=["Mismagius", "Stage 1", "Mismagius"],
    subtypes=["Stage 1"],
    collector_number=5,
    set_code="HGSS2",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    resistance_type=PokemonTypes.COLORLESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Misdreavus.Name",
    family_id=200,
    abilities=[
        Ability(
            title="Magical Trans",
            game_text="Once during your turn (before your attack), you may move a Psychic Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Mismagius is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_move_available,
            effect=move_energy_between(predicate=_is_psychic_energy, count=1),
        ),
        Attack(
            title="Psychic Pulse",
            game_text="Does 10 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)