from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="9347009f-f8be-55c0-b53a-be000ab157b0",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Skeledirgeex.Name",
    display_name="Skeledirge ex",
    searchable_by=["Skeledirge ex", "Stage 2", "Tera", "ex", "Skeledirgeex"],
    subtypes=["Stage 2", "Tera", "ex"],
    collector_number=137,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=330,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Crocalor.Name",
    family_id=909,
    abilities=[
        Ability(
            title="Incendiary Song",
            game_text="Once during your turn, you may discard a Basic Fire Energy card from your hand in order to use this Ability. During this turn, attacks used by your Pok\u00e9mon do 60 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Luster Burn",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 2},
            damage=160,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)