from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    discard_stadium_attack,
    ignore_modifier_attack,
)
from ptcgo.game.card_effects.passives_common import is_in_active_spot, takes_less_passive


def _protects_own_team(target, carrier) -> bool:
    return (target.owning_player_id == carrier.owning_player_id
            and is_in_active_spot(carrier))

card = PokemonCardDef(
    guid="dd6ae83c-17d8-5a4b-b3b9-1dc5ca9fb233",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.FlygonGX.Name",
    display_name="Flygon-GX",
    searchable_by=["Flygon-GX", "Stage 2", "GX", "FlygonGX"],
    subtypes=["Stage 2", "GX"],
    collector_number=256,
    set_code="SM12",
    rarity=Rarities.RareRainbow,
    hp=240,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name",
    family_id=328,
    abilities=[
        Ability(
            title="Dusty Defense",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, all of your Pok\u00e9mon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=takes_less_passive(30, protects=_protects_own_team),
        ),
        Attack(
            title="Desert Hurricane",
            game_text="If there is any Stadium card in play, this attack does 120 more damage. Then, discard that Stadium card.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=120,
            damage_operator="+",
            effect=discard_stadium_attack(bonus=120),
        ),
        Attack(
            title="Sonic Edge-GX",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.FIGHTING: 3},
            damage=220,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)