from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.passives_common import is_in_active_spot
from ptcgo.game.session.passives import Passive, carrier_pokemon


class ReversalAuraPassive(Passive):
    """While its owner has more Prize cards left than the opponent: Hariyama's
    attacks do 20 more to the Active Pokemon, and the opponent's Active does
    20 less damage to Hariyama."""

    @staticmethod
    def _ahead(carrier, board) -> bool:
        owner = carrier.owning_player_id
        rivals = [pid for pid in (getattr(board, "player_ids", None) or [])
                  if pid != owner]
        if not rivals:
            return False

        def remaining(pid):
            area = board.find_player_area(pid, "prizePile")
            return len(area.children) if area else 0

        return remaining(owner) > remaining(rivals[0])

    def modify_damage_dealt(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or not calc.is_attack or calc.attacker is not holder:
            return
        if not (calc.to_active and calc.is_opposing):
            return
        if self._ahead(holder, calc.board):
            calc.amount += 20

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.target is not holder:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if calc.attacker is None or not is_in_active_spot(calc.attacker):
            return
        if self._ahead(holder, calc.board):
            calc.amount = max(0, calc.amount - 20)


card = PokemonCardDef(
    guid="b36d6310-f054-5cd7-8b59-a43b43bf714c",
    key="EX11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hariyama.Name",
    display_name="Hariyama",
    searchable_by=["Hariyama", "Stage 1", "Hariyama"],
    subtypes=["Stage 1"],
    collector_number=44,
    set_code="EX11",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Makuhita.Name",
    family_id=296,
    abilities=[
        Ability(
            title="Reversal Aura",
            game_text="As long as you have more Prize cards left than your opponent, each of Hariyama's attacks does 20 more damage to the Active Pok\u00e9mon (before applying Weakness and Resistance) and damage done by the Active Pok\u00e9mon to Hariyama is reduced by 20 (after applying Weakness and Resistance).",
            passive=ReversalAuraPassive(),
        ),
        Attack(
            title="Slap Push",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
        ),
        Attack(
            title="Brick Smash",
            game_text="This attack's damage isn't affected by Resistance, Pok\u00e9-Powers, Pok\u00e9-Bodies, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=ignore_modifier_attack(ignore_resistance=True, ignore_target_effects=True),
        ),
    ],
)