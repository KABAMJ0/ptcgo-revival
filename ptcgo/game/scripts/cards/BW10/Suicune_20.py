from ptcgo.game.card_effects.passives_common import (
    attacker_is_gx_or_ex, damage_shield_from,
)
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


card = PokemonCardDef(
    guid="79229abf-9daa-5727-b829-f45bbce4b935",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Suicune.Name",
    display_name="Suicune",
    searchable_by=["Suicune", "Basic", "Suicune"],
    subtypes=["Basic"],
    collector_number=20,
    set_code="BW10",
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=245,
    abilities=[
        Ability(
            title="Safeguard",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by Pok\u00e9mon-EX.",
            passive=damage_shield_from(attacker_is_gx_or_ex()),
        ),
        Attack(
            title="Aurora Beam",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)