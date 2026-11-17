from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="96df9775-c78d-56c7-82a7-b7c88af5a3a5",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Regigigas.Name",
    display_name="Regigigas",
    searchable_by=["Regigigas", "Basic", "Regigigas"],
    subtypes=["Basic"],
    collector_number=84,
    set_code="SM4",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=486,
    abilities=[
        Ability(
            title="Seal of Antiquity",
            game_text="This Pok\u00e9mon can't attack unless Regirock, Regice, and Registeel are on your Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Giant Stomp",
            game_text="Discard any Stadium card in play.",
            cost={PokemonTypes.COLORLESS: 5},
            damage=160,
            effect=unimplemented,
        ),
    ],
)