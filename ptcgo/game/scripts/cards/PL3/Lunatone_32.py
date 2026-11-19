from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.passives_common import (
    attack_shield_from, side_has_named, team_of_names,
)
from ptcgo.game.card_effects.trainers import pokemon_lv_x


def _is_lv_x():
    """Attacker pred: a Pokemon LV.X. The corpus prints the subtype as
    "Level-Up", so `pokemon_lv_x` accepts every spelling."""
    return pokemon_lv_x()
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="05580b66-e474-5c29-be47-ac0f936dd4a4",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lunatone.Name",
    display_name="Lunatone",
    searchable_by=["Lunatone", "Basic", "Lunatone"],
    subtypes=["Basic"],
    collector_number=32,
    set_code="PL3",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=337,
    abilities=[
        Ability(
            title="Marvel Eyes",
            game_text="If you have Solrock in play, prevent all effects of attacks, including damage, done to any of your Lunatone or Solrock by your opponent's Pok\u00e9mon LV.X.",
            passive=attack_shield_from(
                _is_lv_x(), protects=team_of_names("lunatone", "solrock"),
                effects_too=True,
                when=lambda board, carrier: side_has_named(
                    board, carrier.owning_player_id, "solrock")),
        ),
        Attack(
            title="Gravity Wave",
            game_text="Does 30 damage to each of your opponent's Benched Pok\u00e9mon that doesn't have a Retreat Cost. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
    ],
)