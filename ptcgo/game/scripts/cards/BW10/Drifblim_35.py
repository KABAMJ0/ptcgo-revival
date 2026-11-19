from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_opponent_energy_attack
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import has_team_plasma
from ptcgo.game.session.passives import Passive, carrier_pokemon


class DriftingBalloonPassive(Passive):
    """Attacks cost [C] less per opposing Team Plasma Pokemon in play."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        owner = pokemon.owning_player_id
        plasma = sum(1 for pid in board.player_ids if pid != owner
                     for other in board.pokemon_in_play(pid)
                     if has_team_plasma(board, other))
        if plasma <= 0 or "Colorless" not in cost:
            return cost
        remaining = cost["Colorless"] - plasma
        if remaining > 0:
            cost["Colorless"] = remaining
        else:
            del cost["Colorless"]
        return cost


card = PokemonCardDef(
    guid="28b352c7-d613-594a-943a-eea0c50ed5c9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Drifblim.Name",
    display_name="Drifblim",
    searchable_by=["Drifblim", "Stage 1", "Drifblim"],
    subtypes=["Stage 1"],
    collector_number=35,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drifloon.Name",
    family_id=425,
    abilities=[
        Ability(
            title="Drifting Balloon",
            game_text="This Pok\u00e9mon's attacks cost Colorless less for each of your opponent's Team Plasma Pok\u00e9mon in play.",
            passive=DriftingBalloonPassive(),
        ),
        Attack(
            title="Derail",
            game_text="Discard a Special Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=discard_opponent_energy_attack(1, special_only=True),
        ),
    ],
)