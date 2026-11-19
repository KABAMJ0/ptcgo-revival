from ptcgo.game.card_effects.trainers import is_energy_card
from ptcgo.game.session.passives import Passive, carrier_pokemon
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

class ShellRetreatPassive(Passive):
    """While any Energy is attached, damage done to Squirtle by an opponent's
    attack is reduced by 10 (after W/R)."""

    def modify_damage_taken(self, calc, carrier):
        holder = carrier_pokemon(carrier)
        if holder is None or calc.target is not holder:
            return
        if not (calc.is_attack and calc.is_opposing):
            return
        if any(is_energy_card(child) for child in holder.children):
            calc.amount = max(0, calc.amount - 10)

card = PokemonCardDef(
    guid="0b00b401-0109-5c60-a2bc-9b5935dd66ff",
    key="EX4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squirtle.Name",
    display_name="Squirtle",
    searchable_by=["Squirtle", "Basic", "Squirtle"],
    subtypes=["Basic"],
    collector_number=46,
    set_code="EX4",
    rarity=Rarities.Common,
    hp=50,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=7,
    abilities=[
        Ability(
            title="Shell Retreat",
            game_text="As long as Squirtle has any Energy cards attached to it, damage done to Squirtle by an opponent's attack is reduced by 10 (after applying Weakness and Resistance).",
            passive=ShellRetreatPassive(),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
        ),
    ],
)