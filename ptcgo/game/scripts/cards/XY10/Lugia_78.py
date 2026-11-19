from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import bonus_if
from ptcgo.game.card_effects.trainers import is_pokemon_EX
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="afd5b1be-e4db-5a50-bc6f-c70778a9503a",
    key="XY10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lugia.Name",
    display_name="Lugia",
    searchable_by=["Lugia", "Basic", "Lugia"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="XY10",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Pressure",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, any damage done by attacks from your opponent's Active Pok\u00e9mon is reduced by 20 (before applying Weakness and Resistance).",
            effect=unimplemented,
        ),
        Attack(
            title="Intensifying Burn",
            game_text="If your opponent's Active Pok\u00e9mon is a Pok\u00e9mon-EX, this attack does 60 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=bonus_if(lambda ctx: is_pokemon_EX(ctx.defender), 60),
        ),
    ],
)