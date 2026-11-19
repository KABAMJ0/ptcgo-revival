from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import attack_effect_shield_passive
from ptcgo.game.card_effects.trainers import combined, holder_ability_shield

card = PokemonCardDef(
    guid="f45e7725-690a-576c-a33e-b86a99f4f743",
    key="ME5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Poltchageist.Name",
    display_name="Poltchageist",
    searchable_by=["Poltchageist", "Basic", "Poltchageist"],
    subtypes=["Basic"],
    collector_number=5,
    set_code="ME5",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    family_id=1012,
    abilities=[
        Ability(
            title="Hide 'n' Sneak",
            game_text="Prevent all effects of your opponent's Pok\u00e9mon's attacks and Abilities done to this Pok\u00e9mon. (Damage is not an effect.)",
            passive=combined(attack_effect_shield_passive(), holder_ability_shield()),
        ),
        Attack(
            title="Furtive Drop",
            game_text="Place 1 damage counter on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)