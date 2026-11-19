from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="b0854c9f-841e-5413-a7d4-e4a9b4c6bd02",
    key="ME6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Thundurus.Name",
    display_name="Thundurus",
    searchable_by=["Thundurus", "Basic", "Thundurus"],
    subtypes=["Basic"],
    collector_number=35,
    set_code="ME6",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=642,
    abilities=[
        Ability(
            title="Incarnate Solidarity",
            game_text="If you have Tornadus, Thundurus, Landorus, and Enamorus in play, ignore all Colorless Energy in the costs of attacks used by this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Thunderous Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)