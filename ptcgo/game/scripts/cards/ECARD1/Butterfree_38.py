from ptcgo.game.card_effects.support_common import cure_conditions_effect
from ptcgo.game.card_effects.passives_common import unafflicted
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Activations
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3b93eb8d-510b-59e0-b1b2-d3b37f3ef988",
    key="ECARD1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=38,
    set_code="ECARD1",
    rarity=Rarities.Rare,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Ability(
            title="Miraculous Powder",
            game_text="Once during your turn (before your attack), you may remove all Special Conditions from your Active Pok\u00e9mon. This power can't be used if Butterfree is affected by a Special Condition.",
            activation=Activations.ONCE_PER_TURN,
            condition=unafflicted,
            effect=cure_conditions_effect(scope="active"),
        ),
        Attack(
            title="Spiral Drain",
            game_text="Flip a coin. If heads, remove 2 damage counters from Butterfree.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=unimplemented,
        ),
    ],
)