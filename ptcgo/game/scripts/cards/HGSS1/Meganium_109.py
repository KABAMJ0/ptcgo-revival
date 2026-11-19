from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.card_effects.pokemon import energy_provides_type
from ptcgo.game.card_effects.support_common import move_energy_between

GRASS = PokemonTypes.GRASS.value


def _is_grass_energy(card):
    return energy_provides_type(card, GRASS)


def _move_available(board, player_id, pokemon):
    if pokemon.get_attribute(AttrID.SPECIAL_CONDITIONS):
        return False
    holders = [p for p in board.pokemon_in_play(player_id)
               if any(_is_grass_energy(e) for e in board.attached_energies(p))]
    return bool(holders) and len(board.pokemon_in_play(player_id)) >= 2


card = PokemonCardDef(
    guid="d36510d8-0f42-5471-a5cc-c3ad3f277b77",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Prime", "Meganium"],
    subtypes=["Stage 2", "Prime"],
    collector_number=109,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Leaf Trans",
            game_text="As often as you like during your turn (before your attack), you may move a Grass Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Meganium is affected by a Special Condition.",
            activation=Activations.UNLIMITED,
            condition=_move_available,
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)