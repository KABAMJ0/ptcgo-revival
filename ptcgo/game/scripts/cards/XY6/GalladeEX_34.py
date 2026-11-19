from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="250f6b57-c178-51cd-a598-37e7d7dcf442",
    key="XY6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeEX.Name",
    display_name="Gallade-EX",
    searchable_by=["Gallade-EX", "Basic", "EX", "GalladeEX"],
    subtypes=["Basic", "EX"],
    collector_number=34,
    set_code="XY6",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=475,
    abilities=[
        Attack(
            title="Swift Lunge",
            game_text="You may have your opponent switch his or her Active Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=gust_attack(damage_to_new_active=0, opponent_chooses=True),
        ),
        Attack(
            title="Piercing Prizes",
            game_text="This attack does 20 more damage for each of your remaining Prize cards.",
            cost={PokemonTypes.PSYCHIC: 3},
            damage=50,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)