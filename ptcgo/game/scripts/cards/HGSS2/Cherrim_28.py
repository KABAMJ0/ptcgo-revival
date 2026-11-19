from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.passives_common import heal_activation

_sunny_effect, _sunny_condition = heal_activation(10)


card = PokemonCardDef(
    guid="df322d25-85b3-5b93-8354-342a36217add",
    key="HGSS2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cherrim.Name",
    display_name="Cherrim",
    searchable_by=["Cherrim", "Stage 1", "Cherrim"],
    subtypes=["Stage 1"],
    collector_number=28,
    set_code="HGSS2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cherubi.Name",
    family_id=420,
    abilities=[
        Ability(
            title="Sunny Heal",
            game_text="Once during your turn (before your attack), you may remove 1 damage counter from your Active Pok\u00e9mon. This power can't be used if Cherrim is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=_sunny_condition,
            effect=_sunny_effect,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
        ),
    ],
)