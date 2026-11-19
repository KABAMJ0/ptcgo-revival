from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import (
    carrier_pokemon, is_in_active_spot, prevent_damage_when,
)


def _bench_hit(calc, carrier):
    holder = carrier_pokemon(carrier)
    return (calc.is_attack and calc.is_opposing
            and calc.target.owning_player_id == carrier.owning_player_id
            and not is_in_active_spot(calc.target)
            and is_in_active_spot(holder))

card = PokemonCardDef(
    guid="c12de612-aced-59aa-b98d-bbbd69428703",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=139,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Adverse Weather",
            game_text="As long as this Pok\u00e9mon is in the Active Spot, prevent all damage done to your Benched Pok\u00e9mon by attacks from your opponent's Pok\u00e9mon.",
            passive=prevent_damage_when(_bench_hit),
        ),
        Attack(
            title="Gigantic Bolt",
            game_text="This Pok\u00e9mon also does 90 damage to itself.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=140,
            effect=recoil_attack(90),
        ),
    ],
)