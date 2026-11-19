from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="ea3e94a7-af76-5bb6-8ef4-93a81bd23891",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zeraora.Name",
    display_name="Zeraora",
    searchable_by=["Zeraora", "Basic", "Zeraora"],
    subtypes=["Basic"],
    collector_number=55,
    set_code="SV7",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=807,
    abilities=[
        Attack(
            title="Combat Thunder",
            game_text="This attack does 20 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=20, base=20),
        ),
    ],
)