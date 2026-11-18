from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="23b02669-c934-5ed1-8d1c-85068646dd6a",
    key="XY3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.DragoniteEX.Name",
    display_name="Dragonite-EX",
    searchable_by=["Dragonite-EX", "Basic", "EX", "DragoniteEX"],
    subtypes=["Basic", "EX"],
    collector_number=74,
    set_code="XY3",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    family_id=149,
    abilities=[
        Ability(
            title="Bust In",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench, you may move any number of basic Energy attached to your Pok\u00e9mon to this Pok\u00e9mon. If you do, switch this Pok\u00e9mon with your Active Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Jet Sonic",
            game_text="You may discard an Energy attached to this Pok\u00e9mon. If you do, this attack does 40 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.LIGHTNING: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)