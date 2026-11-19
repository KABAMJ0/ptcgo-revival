from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import move_energy_between
from ptcgo.game.card_effects.trainers import is_basic_energy_card, team_magma_target


def _magma_switch_condition(board, player_id, pokemon) -> bool:
    """A basic Energy on one of your Pokemon and a different Team Magma
    Pokemon to receive it."""
    mine = board.pokemon_in_play(player_id)
    receivers = [p for p in mine if team_magma_target(p)]
    holders = [p for p in mine
               if any(is_basic_energy_card(e)
                      for e in board.attached_energies(p))]
    return any(holder is not receiver
               for holder in holders for receiver in receivers)


def _is_team_magma(pokemon, ctx) -> bool:
    return team_magma_target(pokemon)


card = PokemonCardDef(
    guid="6e8067ee-5346-5caf-9acb-1d9b0f02f058",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasClaydol.Name",
    display_name="Team Magma's Claydol",
    searchable_by=["Team Magma's Claydol", "Stage 1", "TeamMagmasClaydol"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasBaltoy.Name",
    family_id=343,
    abilities=[
        Ability(
            title="Magma Switch",
            game_text="Once during your turn (before your attack), you may move a basic Energy from 1 of your Pok\u00e9mon to 1 of your Team Magma Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            condition=_magma_switch_condition,
            effect=move_energy_between(
                predicate=is_basic_energy_card, count=1,
                from_pool="any", to_pool="any", to_pred=_is_team_magma,
                prompt="Choose a basic Energy to move to a Team Magma Pok\u00e9mon"),
        ),
        Attack(
            title="Power Beam",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)
