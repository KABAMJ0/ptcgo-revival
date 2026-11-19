from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack
from ptcgo.game.card_effects.passives_common import item_or_supporter_effect_shield



card = PokemonCardDef(
    guid="58d3993c-e4b7-5095-8e5c-2e13064c23c9",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cetitanex.Name",
    display_name="Cetitan ex",
    searchable_by=["Cetitan ex", "Stage 1", "ex", "Cetitanex"],
    subtypes=["Stage 1", "ex"],
    collector_number=210,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=300,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=4,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cetoddle.Name",
    family_id=974,
    abilities=[
        Ability(
            title="Snow Camouflage",
            game_text="Whenever your opponent plays an Item or Supporter card from their hand, prevent all effects of that card done to this Pok\u00e9mon.",
            passive=item_or_supporter_effect_shield(),
        ),
        Attack(
            title="Crushing Press",
            game_text="You may discard a Stadium in play. If you do, this attack does 140 more damage.",
            cost={PokemonTypes.WATER: 3, PokemonTypes.COLORLESS: 1},
            damage=140,
            damage_operator="+",
            effect=discard_stadium_attack(optional=True, bonus=140),
        ),
    ],
)