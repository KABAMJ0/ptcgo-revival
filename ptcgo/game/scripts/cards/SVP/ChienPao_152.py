from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import return_attached_energy

card = PokemonCardDef(
    guid="cef4db35-21c7-5fe7-8783-33e8b7c550db",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChienPao.Name",
    display_name="Chien-Pao",
    searchable_by=["Chien-Pao", "Basic", "ChienPao"],
    subtypes=["Basic"],
    collector_number=152,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=120,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    family_id=1002,
    abilities=[
        Ability(
            title="Snow Sink",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may discard a Stadium in play.",
            effect=unimplemented,
        ),
        Attack(
            title="Icicle Loop",
            game_text="Put an Energy attached to this Pok\u00e9mon into your hand.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=return_attached_energy(count=1, to="hand", target="self"),
        ),
    ],
)