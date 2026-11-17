from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f694d824-8517-5d9a-91ad-9d66bb4493fa",
    key="EX13",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Persian.Name",
    display_name="Persian δ",
    searchable_by=["Persian \u03b4", "Stage 1", "Persian"],
    subtypes=["Stage 1"],
    collector_number=48,
    set_code="EX13",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.DARKNESS, PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Meowth.Name",
    family_id=53,
    abilities=[
        Attack(
            title="Scratch and Draw",
            game_text="If any Stadium card with Holon in its name is in play, draw 3 cards.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=unimplemented,
        ),
        Attack(
            title="Deceive",
            game_text="Your opponent chooses 1 of his or her Pok\u00e9mon. Put 4 damage counters on that Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)