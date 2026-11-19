from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack
from ptcgo.game.card_effects.passives_common import damage_shield_from
from ptcgo.game.card_effects.trainers import attacker_has_ability

card = PokemonCardDef(
    guid="6cfdbce4-7998-51b1-9dfc-958a9db294f1",
    key="BW9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LatiasEX.Name",
    display_name="Latias-EX",
    searchable_by=["Latias-EX", "Basic", "EX", "LatiasEX"],
    subtypes=["Basic", "EX"],
    collector_number=112,
    set_code="BW9",
    rarity=Rarities.RareUltra,
    hp=160,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DRAGON,
    family_id=380,
    abilities=[
        Ability(
            title="Bright Down",
            game_text="Prevent all effects of attacks, including damage, done to this Pok\u00e9mon by your opponent's Pok\u00e9mon with Abilities.",
            passive=damage_shield_from(attacker_has_ability()),
        ),
        Attack(
            title="Barrier Break",
            game_text="This attack's damage isn't affected by Weakness, Resistance, or any other effects on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=70,
            effect=ignore_modifier_attack(ignore_weakness=True, ignore_resistance=True),
        ),
    ],
)