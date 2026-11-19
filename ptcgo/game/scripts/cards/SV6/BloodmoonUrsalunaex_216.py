from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack
from ptcgo.game.session.passives import Passive, carrier_pokemon

class _SeasonedSkill(Passive):
    """Blood Moon costs [C] less for each Prize card the opponent has taken."""

    def modify_attack_cost(self, cost, pokemon, carrier, board):
        if carrier_pokemon(carrier) is not pokemon:
            return cost
        opponents = [pid for pid in board.player_ids
                     if pid != pokemon.owning_player_id]
        if not opponents or "Colorless" not in cost:
            return cost
        taken = board.prizes_taken(opponents[0])
        if taken <= 0:
            return cost
        cost["Colorless"] = max(0, cost["Colorless"] - taken)
        return cost

card = PokemonCardDef(
    guid="51953cab-21b8-5577-bbe0-2624582bec20",
    key="SV6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BloodmoonUrsalunaex.Name",
    display_name="Bloodmoon Ursaluna ex",
    searchable_by=["Bloodmoon Ursaluna ex", "Basic", "ex", "BloodmoonUrsalunaex"],
    subtypes=["Basic", "ex"],
    collector_number=216,
    set_code="SV6",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=901,
    abilities=[
        Ability(
            title="Seasoned Skill",
            game_text="Blood Moon used by this Pok\u00e9mon costs Colorless less for each Prize card your opponent has taken.",
            passive=_SeasonedSkill(),
        ),
        Attack(
            title="Blood Moon",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=240,
            effect=lock_self_attack(),
        ),
    ],
)