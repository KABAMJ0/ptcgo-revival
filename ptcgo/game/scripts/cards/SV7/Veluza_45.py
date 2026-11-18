from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import ignore_modifier_attack

card = PokemonCardDef(
    guid="74f837a7-7e64-576d-bf50-202e8fe3bfe1",
    key="SV7",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Veluza.Name",
    display_name="Veluza",
    searchable_by=["Veluza", "Basic", "Veluza"],
    subtypes=["Basic"],
    collector_number=45,
    set_code="SV7",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=976,
    abilities=[
        Ability(
            title="Food Prep",
            game_text="Attacks used by this Pok\u00e9mon cost Colorless less for each Kofu card in your discard pile.",
            effect=unimplemented,
        ),
        Attack(
            title="Sonic Edge",
            game_text="This attack's damage isn't affected by any effects on your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 4},
            damage=110,
            effect=ignore_modifier_attack(ignore_target_effects=True),
        ),
    ],
)