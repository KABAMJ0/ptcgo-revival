from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="36f7d1aa-a893-5473-b920-a4edb2d010fb",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bouffalant.Name",
    display_name="Bouffalant",
    searchable_by=["Bouffalant", "Basic", "Bouffalant"],
    subtypes=["Basic"],
    collector_number=136,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=626,
    abilities=[
        Ability(
            title="Curly Wall",
            game_text="As long as you have at least 1 other Bouffalant in play, all of your Basic Colorless Pok\u00e9mon take 60 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance). The effect of Curly Wall doesn't stack.",
            effect=unimplemented,
        ),
        Attack(
            title="Boundless Power",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=130,
            effect=lock_self_attack(),
        ),
    ],
)