from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="dda2c9b8-cfe6-5258-9aec-75c00f83cf05",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Infernape.Name",
    display_name="Infernape",
    searchable_by=["Infernape", "Stage 2", "Infernape"],
    subtypes=["Stage 2"],
    collector_number=31,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Monferno.Name",
    family_id=390,
    abilities=[
        Attack(
            title="Rushing Flames",
            game_text="Discard as many Fire Energy cards as you like attached to your Pok\u00e9mon in play. Flip a coin for each Energy card you discarded. This attack does 80 damage times the number of heads.",
            cost={PokemonTypes.FIRE: 1},
            damage=80,
            damage_operator="x",
            effect=unimplemented,
        ),
        Attack(
            title="Rage",
            game_text="Does 30 damage plus 10 more damage for each damage counter on Infernape.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)