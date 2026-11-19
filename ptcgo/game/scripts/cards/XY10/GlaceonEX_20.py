from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities
from ptcgo.game.card_effects.passives_common import attacker_is_basic, attacker_is_evolution, protect_next_turn

card = PokemonCardDef(
    guid="d1de258b-0622-53e4-9137-d5cda537ba31",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GlaceonEX.Name",
    display_name="Glaceon-EX",
    searchable_by=["Glaceon-EX", "Basic", "EX", "GlaceonEX"],
    subtypes=["Basic", "EX"],
    collector_number=20,
    set_code="XY10",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=471,
    abilities=[
        Attack(
            title="Second Bite",
            game_text="This attack does 10 more damage for each damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=20),
        ),
        Attack(
            title="Crystal Ray",
            game_text="During your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks from Evolution Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=protect_next_turn(prevent=True, attacker_pred=attacker_is_evolution()),
        ),
    ],
)