from ptcgo.game.card_effects.attacks_common import recoil_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="09c3aef5-c560-5062-89f4-9e9c2e664a20",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Houndoomex.Name",
    display_name="Houndoom ex",
    searchable_by=["Houndoom ex", "Stage 1", "ex", "Houndoomex"],
    subtypes=["Stage 1", "ex"],
    collector_number=103,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=270,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Houndour.Name",
    family_id=229,
    abilities=[
        Attack(
            title="Evil Claw",
            game_text="If the Defending Pok\u00e9mon is a Basic Pok\u00e9mon, it can't attack during your opponent's next turn.",
            cost={PokemonTypes.DARKNESS: 2},
            damage=90,
            effect=unimplemented,
        ),
        Attack(
            title="Hound's Fang",
            game_text="This Pok\u00e9mon also does 30 damage to itself.",
            cost={PokemonTypes.DARKNESS: 3},
            damage=220,
            effect=recoil_attack(30),
        ),
    ],
)