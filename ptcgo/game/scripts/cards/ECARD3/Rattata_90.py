from ptcgo.game.card_effects.attacks_common import condition_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities, SpecialConditions
from ptcgo.game.card_effects.attacks_common import condition_attack

card = PokemonCardDef(
    guid="c2aca0bc-8edb-5462-9b71-43ab3585568d",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Rattata.Name",
    display_name="Rattata",
    searchable_by=["Rattata", "Basic", "Rattata"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="ECARD3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=19,
    abilities=[
        Attack(
            title="Call for Friends",
            game_text="Search your deck for a Baby Pok\u00e9mon or Basic Pok\u00e9mon card and put it onto your Bench. Shuffle your deck afterward. (You can't use this attack if your Bench is full.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Body Slam",
            game_text="Flip a coin. If heads, the Defending Pok\u00e9mon is now Paralyzed.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=condition_attack(SpecialConditions.PARALYZED, flip=True),
        ),
    ],
)