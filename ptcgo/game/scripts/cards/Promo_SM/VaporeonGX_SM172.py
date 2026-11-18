from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Activations, unimplemented
from ptcgo.game.card_effects.passives_common import heal_activation
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, AttrID

_heal, _heal_condition = heal_activation(30, target_pred=lambda p: PokemonTypes.WATER.value in (
    p.get_attribute(AttrID.POKEMON_TYPES) or []
))


card = PokemonCardDef(
    guid="10b9217c-fcec-5f3c-8db6-c4ce6e7ac44c",
    key="Promo_SM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.VaporeonGX.Name",
    display_name="Vaporeon-GX",
    searchable_by=["Vaporeon-GX", "Stage 1", "GX", "VaporeonGX"],
    subtypes=["Stage 1", "GX"],
    collector_number=172,
    set_code="Promo_SM",
    rarity=Rarities.RarePromo,
    hp=210,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Eevee.Name",
    family_id=133,
    abilities=[
        Ability(
            title="Hydrating Drops",
            game_text="Once during your turn (before your attack), you may heal 30 damage from your Active Water Pok\u00e9mon.",
            activation=Activations.ONCE_PER_TURN,
            effect=_heal,
            condition=_heal_condition,
        ),
        Attack(
            title="Hydro Pump",
            game_text="This attack does 30 more damage times the amount of Water Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            damage_operator="+",
            effect=unimplemented,
        ),
        Attack(
            title="Cure Shower-GX",
            game_text="Heal all damage from all of your Water Pok\u00e9mon. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.WATER: 1},
            effect=unimplemented,
        ),
    ],
)