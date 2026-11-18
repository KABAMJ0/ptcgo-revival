from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="12199818-bb00-51c0-8685-4b63ad3ffa50",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bellibolt.Name",
    display_name="Bellibolt",
    searchable_by=["Bellibolt", "Stage 1", "Bellibolt"],
    subtypes=["Stage 1"],
    collector_number=78,
    set_code="SV3",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name",
    family_id=938,
    abilities=[
        Ability(
            title="Insulator",
            game_text="Prevent all damage done to this Pok\u00e9mon by attacks from your opponent's Lightning Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)