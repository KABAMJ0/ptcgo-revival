from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4cbcba1d-90e7-5986-8609-fc3d13ef4c2f",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zangooseex.Name",
    display_name="Zangoose ex",
    searchable_by=["Zangoose ex", "Basic", "ex", "Zangooseex"],
    subtypes=["Basic", "ex"],
    collector_number=167,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=200,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=335,
    abilities=[
        Attack(
            title="Spike Draw",
            game_text="Draw 2 cards.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Wild Scissors",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=180,
            effect=recoil_attack(30),
        ),
    ],
)