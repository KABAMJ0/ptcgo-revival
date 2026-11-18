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
    guid="efa17d72-16d5-5828-b664-dcd8752302d8",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=70,
    set_code="SV3",
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
            effect=unimplemented,
        ),
    ],
)