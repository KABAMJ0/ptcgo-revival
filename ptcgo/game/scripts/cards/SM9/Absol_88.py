from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.session.passives import effective_retreat_cost
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="7611cbed-f87c-5eb4-aef0-387aca6979bb",
    key="SM9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Absol.Name",
    display_name="Absol",
    searchable_by=["Absol", "Basic", "Absol"],
    subtypes=["Basic"],
    collector_number=88,
    set_code="SM9",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=359,
    abilities=[
        Ability(
            title="Dark Ambition",
            game_text="If your opponent's Active Pok\u00e9mon is a Basic Pok\u00e9mon, its Retreat Cost is Colorless more.",
            effect=damage_per(lambda c: effective_retreat_cost(c.board, c.defender), 30),
        ),
        Attack(
            title="Shadow Seeker",
            game_text="This attack does 30 more damage for each Colorless in your opponent's Active Pok\u00e9mon's Retreat Cost.",
            cost={PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)